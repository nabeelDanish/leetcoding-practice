from typing import List


class Solution:
    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     task_qty = {}
    #     for task in tasks:
    #         if task not in task_qty:
    #             task_qty[task] = 1
    #         else:
    #             task_qty[task] += 1

    #     interval_count = {}
    #     for task in task_qty.keys():
    #         interval_count[task] = 0

    #     order_of_tasks = []
    #     for task, qty in task_qty.items():
    #         order_of_tasks.append([task, qty])

    #     order_of_tasks = sorted(order_of_tasks, key=lambda x: x[1], reverse=True)

    #     steps = 0
    #     tasks_remaining = len(tasks)
    #     m = len(order_of_tasks)
    #     # order = 0

    #     while True:
    #         selected_task = None
    #         # i = order
    #         # while True:
    #         for pair in order_of_tasks:
    #             # pair = order_of_tasks[i]
    #             task, qty = pair[0], pair[1]

    #             # if we can't use this task because it is finished, we skip
    #             if qty <= 0:
    #                 continue
    #                 # i += 1
    #                 # if i >= m:
    #                 #     i = 0
    #                 # if i == order:
    #                 #     order += 1
    #                 #     if order > m:
    #                 #         order = 0
    #                 #     break
    #                 # continue

    #             # check if we can use this task based on interval
    #             if interval_count.get(task) == 0:
    #                 selected_task = task
    #                 pair[1] -= 1
    #                 # order = i + 1
    #                 # if order >= m:
    #                 #     order = 0
    #                 break

    #             # i += 1
    #             # if i >= m:
    #             #     i = 0

    #             # if i == order:
    #             #     break

    #         steps += 1

    #         # update the interval of any previously selected task
    #         for task, interval in interval_count.items():
    #             if task == selected_task:
    #                 interval_count[task] += 1
    #             elif interval > 0:
    #                 interval_count[task] += 1
    #                 if interval_count[task] > n:
    #                     interval_count[task] = 0

    #         # check if all tasks are completed
    #         if selected_task:
    #             tasks_remaining -= 1
    #             if tasks_remaining == 0:
    #                 break

    #     return steps

    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_qty = {}
        for task in tasks:
            if task not in task_qty:
                task_qty[task] = 1
            else:
                task_qty[task] += 1

        cooldown_count = {}
        for task in task_qty.keys():
            cooldown_count[task] = 0

        steps = 0
        tasks_remaining = len(tasks)

        while True:
            selected_task = None
            tasks_with_no_cooldown = []

            # find all the tasks that have zero cooldown
            for task, cooldown in cooldown_count.items():
                if cooldown == 0:
                    tasks_with_no_cooldown.append(task)

            # if no task has zero cooldown we skip, if we have a list we select the one that has the max count
            if tasks_with_no_cooldown:
                tasks_qty_list = []
                for task in tasks_with_no_cooldown:
                    tasks_qty_list.append([task, task_qty.get(task)])

                # sort to find the one with the most quantity
                best_task = None
                max_qty = 0
                for pair in tasks_qty_list:
                    if pair[1] > max_qty:
                        best_task = pair[0]
                        max_qty = pair[1]
                
                # make sure we actually have quantity for this
                if max_qty > 0:          
                    selected_task = best_task

                    # decrease the quantity of this task
                    task_qty[selected_task] = max(0, task_qty[selected_task] - 1)

                    # set the cooldown to the interval
                    cooldown_count[selected_task] = n

            # Increment the steps to simulate time
            steps += 1

            # decrease the cooldown for all the tasks except the one that was selected
            for task in cooldown_count.keys():
                if task == selected_task:
                    continue

                cooldown_count[task] = max(0, cooldown_count[task] - 1)

            # if task was selected and this is the last one, break
            if selected_task:
                tasks_remaining -= 1
                if tasks_remaining <= 0:
                    break

        return steps

    def testLeastInterval(self, tasks: List[str], n: int, expected: int):
        actual = self.leastInterval(tasks, n)
        if actual == expected:
            print(f"Test Case Passed!")
        else:
            print(f"Test Case Failed! tasks: {tasks}, n: {n}, expected: {expected}, actual: {actual}")


Solution().testLeastInterval(
    ["A", "A", "A", "B", "B", "B"],
    2,
    8
)
Solution().testLeastInterval(
    ["A", "C", "A", "B", "D", "B"],
    1,
    6
)
Solution().testLeastInterval(
    ["A", "A", "A", "B", "B", "B"],
    3,
    10
)
Solution().testLeastInterval(
    ["A", "A", "A", "B", "B", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"],
    7,
    18
)
Solution().testLeastInterval(
    ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"],
    2,
    12
)
