#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;

const int MAXN = 100001;

struct status {
	int n, t;
	status(int n, int t) : n(n), t(t) {};
};

bool visit[MAXN];

int BFS(int n, int k) {
	queue<status> myQueue;
	myQueue.push(status(n, 0));
	visit[n] = true;
	while (!myQueue.empty()) {
		status current = myQueue.front();
		myQueue.pop();
		if (current.n = k) {
			return current.t;
		}
	}
	for (int i = 0 ; i < 3 ; i++) {
		status next(current.n, current.t + 1);
		if (i == 1) {
			next.n += 1;
		}
		else if (i == 2) {
			next.n -= 1;
		}
		else if (i == 3) {
			next.n *= 2;
		}
		if (next.n < 0 || next.n >MAXN || visit[next.n]) {
			continue;
		}
		myQueue.push(next);
		visit[next.n] = true;
	}
}

int main() {
	int n, k;
	scanf("%d%d", &n, &k);
	memset(visit, false, sizeof(visit)); //将visit的值全部初始化为false
	printf("%d\n", BFS(n, k));
	return 0;
}
