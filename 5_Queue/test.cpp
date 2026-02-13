#include <iostream>
// #include <string>
// #include <cstdio>

using namespace std;

int main(){
    //입출력 속도 향상 ( 동기화 해제 )
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // #include <string>
    // 한글자씩 입력 s[i]
    string s;
    getline(cin, s);

    // // #include <cstdio> 
    // // stdio.h 와 같이 scanf, printf 사용 가능
    // int n;
    // scanf("%d", &n);
    // printf("%d\n", n);

    // // 문자열 입력
    // char str[100];
    // char a, b;
    // scanf("%s", str); // 공백 전까지 문자열

    cout << s;

    return 0;
}