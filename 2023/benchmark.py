import numpy as np

from solutions import FINISHED_DAYS
import time
import numpy

N = 25


def main():

    for day_c in FINISHED_DAYS:
        day = day_c()

        print(f"{'='*21} {str(day)} {'='*21}")

        times = []
        for fn in [day.p1, day.p2]:
            result_times = []
            for i in range(N):
                start_time = time.perf_counter()
                result = fn()
                end_time = time.perf_counter()
                result_times.append(end_time - start_time)
            times.append(result_times)

        for idx, _time in enumerate(times):
            print(f"Part {'one' if idx == 0 else 'two'} avg: {np.average(_time):.5f} +/- {np.std(_time):.5f} (seconds) ({N=})")
        print()


    pass

if __name__ == '__main__':
    main()