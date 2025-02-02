#todo match case statement(switch) - an alternative for using many elif statemements
# execute some code if the value matches a case
# benefits: cleaner and syntax is more readable


# def weekdays(day):
#     match day:
#         case 0:
#             return "Monday"
#         case 1:
#             return "Tuesday"
#         case 2:
#             return "Wednesday"
#         case 3:
#             return "Thursday"
#         case 4:
#             return "Friday"
#         case 5:
#             return "Saturday"
#         case 6:
#             return "Sunday"
#         case _:
#             return "Invalid day"
#
# print(weekdays(1))

# def weekdays(day):
#     match day:
#         case 0 | 1 | 2 | 3 | 4:
#             return "Weekday"
#         case 5 | 6:
#             return "Weekend"
#         case _:
#             return "Invalid day"
# print(weekdays(1))

# def weekends(day):
#     match day:
#         case "sunday" | "saturday":
#             return "Weekend"
#         case _:
#             return "Weekday"
# print(weekends("sunday"))