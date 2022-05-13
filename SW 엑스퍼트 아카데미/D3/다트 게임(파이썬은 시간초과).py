''' 파이썬 시간초과'''

T = int(input())
answers = [''] * T
xy_square = [i*i for i in range(201)]

for t in range(1, T+1):
    N = int(input())
    answer = 0
    
    for i in range(N):
        x, y = map(int, input().split())
        x, y = abs(x), abs(y)

        d = xy_square[x] + xy_square[y]
        
        if d <= 400:
            answer += 10
        
        elif d <= 1600:
            answer += 9
        
        elif d <= 3600:
            answer += 8
        
        elif d <= 6400:
            answer += 7
        
        elif d <= 10000:
            answer += 6
        
        elif d <= 14400:
            answer += 5
        
        elif d <= 19600:
            answer += 4
        
        elif d <= 25600:
            answer += 3
        
        elif d <= 32400:
            answer += 2
        
        elif d <= 40000:
            answer += 1
        
        else:
            continue
    
    answers[t-1] = f'#{t} {answer}'

for i in answers:
    print(i)

'''이하 C++로 작성된 코드
#include<iostream>
using namespace std;
     
int main(int argc, char** argv){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    int test_case, T, N, x, y, score, i, d, d2;
    cin >> T;
    for(test_case = 1; test_case <= T; ++test_case)
    {
        score = 0;
        cin >> N;
        for(i = 0; i < N; i++){
            cin >> x >> y;
            d2= x*x+y*y;
             
            for(d = 20; d<=200; d+=20)
                if(d*d >= d2)
                    break;
            score += 11-d/20;
        }
        cout << '#' << test_case << ' ' << score << '\n';
    }
    return 0;
}
'''