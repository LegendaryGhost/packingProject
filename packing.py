from math import inf
from typing import List


class Object1D:
    def __init__(self, size: float):
        self.size = size


class Bac:
    def __init__(self, size: float):
        self.size = size
        self.objects = []

    def add_object(self, obj: Object1D) -> None:
        self.objects.append(obj)

    def objects_size(self) -> float:
        return sum(obj.size for obj in self.objects)

    def may_contain(self, obj: Object1D) -> bool:
        return self.objects_size() + obj.size <= self.size

    def space_left(self):
        return self.size - self.objects_size()


class Packing1D:
    def __init__(self, bac_size: float, objects: List[Object1D]):
        max_obj_size = max(objects, key=lambda obj: obj.size).size
        if max_obj_size > bac_size:
            raise ValueError("Bac size cannot be greater than object size")

        self.bac_size = bac_size
        self.objects = objects

    def best_fit(self) -> List[Bac]:
        bacs = []
        for obj in self.objects:
            best_bac_index = -1
            best_bac_space_left = inf
            for bac_index in range(len(bacs)):
                bac = bacs[bac_index]
                bac_left_space = bac.space_left() - obj.size
                if bac.may_contain(obj) and bac_left_space < best_bac_space_left:
                    best_bac_index = bac_index
                    best_bac_space_left = bac_left_space
            if best_bac_index == -1:
                bacs.append(Bac(self.bac_size))
            bacs[best_bac_index].add_object(obj)

        return bacs
