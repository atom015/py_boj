"""
POT 성공
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	64 MB	420	361	337	86.632%
문제
The teacher has sent an e-mail to her students with the following task:

"Write a programme that will determine and output the value of  if given the statement:

and it holds that ,  to  are integers, and ,  to  one-digit integers." Unfortunately, when the teacher downloaded the task to her computer, the text formatting was lost so the task transformed into a sum of  integers:

For example, without text formatting, the original task in the form of  became a task in the form of . Help the teacher by writing a programme that will, for given  integers from  to  determine and output the value of  from the original task.

Please note: We know that it holds a  ( times).

입력
The first line of input contains the integer  (1 ≤  ≤ 10), the number of the addends from the task. Each of the following  lines contains the integer  (10 ≤  ≤ 9999,  = 1 ... ) from the task.

출력
The first and only line of output must contain the value of  ( ≤ 1 000 000 000) from the original task.

예제 입력 1
2
212
1253
예제 출력 1
1953566
예제 입력 2
5
23
17
43
52
22
예제 출력 2
102
예제 입력 3
3
213
102
45
예제 출력 3
10385
힌트
Clarification of the first example: 212 + 1253 = 441 + 1953125 = 1953566.
"""
s = 0
for i in range(int(input())):
    n = input()
    tmp = int(n[-1])
    s += int(n[0:-1])**tmp
print(s)
