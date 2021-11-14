#include <iostream>
#include <cstdio>
#include <algorithm>
#include <fstream>
#include <cstring>

using namespace std;
const int maxn = 4039;
int p[maxn];
int sum[maxn];
inline int find(int x)
{
    return p[x] == x ? x : p[x] = find(p[x]);
}

int main()
{
    int n;
    while (cin >> n)
    {
        for (int i = 0;i <= maxn; ++i)
        {
            p[i] = i;
            sum[i] = 1;
        }
        FILE* fp;
        fp = freopen("D:\\Desktop\\facebook_combined.txt", "r", stdin);
        for (int i = 0; i < n; ++i)
        {
            int a, b;
            cin >> a >> b;
            int pa = find(a);
            int pb = find(b);
            if (pa != pb)
            {
                p[pa] = pb;
                sum[pb] += sum[pa];
            }
        }
        fclose(fp);
        freopen("CON", "r", stdin);
        
        int maxSum = 1;
        for (int i = 0 ;i <= maxn; ++i)
        {
            if (p[i] == i)
            {
                maxSum = max(maxSum, sum[i]);
            }
        }
        cout << maxSum << endl;
    }
    return 0;
}

