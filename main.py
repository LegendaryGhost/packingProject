from packing import Object1D, Packing1D


def main():
    objects_1d = [
        Object1D(1),
        Object1D(8),
        Object1D(7),
        Object1D(5),
        Object1D(4),
        Object1D(3),
        Object1D(2)
    ]
    bac_size = 10

    packing_1d = Packing1D(bac_size, objects_1d)
    best_fit_bacs = packing_1d.best_fit()

    for bac_index in range(len(best_fit_bacs)):
        bac = best_fit_bacs[bac_index]
        print(f"Bac {bac_index} (size={bac.size}, space left={bac.space_left()}):")
        for obj in bac.objects:
            print(f"\t{obj.size}")
        print("-------------------")


if __name__ == '__main__':
    main()
