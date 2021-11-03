#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

void BFS(int n) {
	queue<long long> myQueue;
	myQueue.push(1);
	while (!myQueue.empty()) {
		long long current = myQueue.front();
		myQueue.pop();
		if (current % n == 0) {
			printf("%lld\n", current);
			return;
		}
		myQueue.push(current * 10);
		myQueue.push(current * 10 + 1);
	}
}

int main() {
	int n;
	while (scanf("%d", &n) != EOF) {
		if (n == 0) {
			break;
		}
		BFS(n);
	}
	return 0;
}