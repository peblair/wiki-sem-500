#
# Copyright 2016 Basis Technology Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os.path
from .utils import decode, similarity

class TestGroup(object):
    def __init__(self, name, cluster, outliers):
        self.name = name
        self.cluster = cluster
        self.outliers = outliers

    def __iter__(self):
        for o in self.outliers:
            yield (self.cluster, o)

    def __len__(self):
        return len(self.outliers)

    def __str__(self):
        return self.name + "\n" + "\n".join(self.cluster) + "\n\n" + "\n".join(self.outliers)

    def is_valid(self):
        return len(self.cluster) > 1 and len(self.outliers) > 0

    def resolve(self, embedding):
        # Keep original name as well for possible debugging information
        filtered_cluster = [(c, embedding[c]) for c in self.cluster if c in embedding]
        filtered_outliers = [(o, embedding[o]) for o in self.outliers if o in embedding]
        return ResolvedTestGroup(embedding, self.name, filtered_cluster, filtered_outliers)

    @staticmethod
    def from_file(filename):
        clustername = os.path.splitext(os.path.basename(filename))[0]
        with open(filename, "rb") as f:
            cluster = []
            outliers = []
            active = cluster
            for line in f:
                line = decode(line).strip()
                if line == "":
                    active = outliers
                    continue
                active.append(line)
            return TestGroup(clustername, cluster, outliers)


class ResolvedTestGroup(TestGroup):
    def __init__(self, embedding, *args, **kwargs):
        TestGroup.__init__(self, *args, **kwargs)
        self.embedding = embedding
        self.pairwise_compactness = {}
        for e1 in self.cluster:
            res = 0.0
            for e2 in (x for x in self.cluster if x != e1):
                res += similarity(e1[1], e2[1])
            self.pairwise_compactness[e1[0]] = res

    def resolve(self):
        raise RuntimeError("Cannot resolve resolved test group")

    def __iter__(self):
        """Yields tuples of the following form:
        ([(cluster-item-name, cluster-item-vec, cluster-item-compactness) ...],
          (outlier-item-name, outlier-item-vec, outlier-item-compactness))"""
        for o in self.outliers:
            outlier_compactness = 0
            with_similarities = []
            for e in self.cluster:
                sim = similarity(e[1], o[1])
                outlier_compactness += sim
                with_similarities.append((e[0], e[1], sim + self.pairwise_compactness[e[0]]))
            yield (with_similarities, (o[0], o[1], outlier_compactness))
