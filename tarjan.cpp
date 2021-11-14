#include<bits/stdc++.h>
using namespace std;
const int maxm=1e6+5;
const int maxn=1e5+5;
int n,v,m,x,f[maxm],t[maxm],head[maxn];
struct edge
{
	int to,nxt;
}e[maxm];
int cnt,dfn[maxn],low[maxn],times,s[maxn],top,instack[maxn];
int col_num,belong[maxn],size[maxn];
void add(int a,int b)
{
	e[++cnt].to=b;
	e[cnt].nxt=head[a];
	head[a]=cnt;
}
void tarjan(int u)
{
	dfn[u]=low[u]=++times;
	instack[u]=1; s[++top]=u;
	for(int i=head[u];i;i=e[i].nxt)
	{
		int to=e[i].to;
		if(!dfn[to])
		{
			tarjan(to);
			low[u]=min(low[u],low[to]);
		}
		else if(instack[to]) low[u]=min(low[u],dfn[to]);
	}
	if(low[u]==dfn[u])
	{
		col_num++;
		do
		{
			size[col_num]++;
			v=s[top--];
			belong[v]=col_num;
			instack[v]=0;
		}while(u!=v);
	}
}
int num[maxm],in[maxn];
bool cmp(int a,int b)
{
	if(f[a]!=f[b]) return f[a]<f[b];
	return t[a]<t[b];
}
void addedge()
{
	for(int i=1;i<=col_num;i++) head[i]=0;
	cnt=0;
	for(int i=1;i<=m;i++)
		f[i]=belong[f[i]],t[i]=belong[t[i]],num[i]=i;
	sort(num+1,num+m+1,cmp);
	for(int i=1;i<=m;i++)
	{
		int now=num[i];
		if(f[now]!=t[now] && (f[now]!=f[num[i-1]] || t[now]!=t[num[i-1]]))
			in[t[now]]++,add(f[now],t[now]);
	}
}
int dis[maxn],ca[maxn],ans;
void topo()
{
	queue <int> q;
	for(int i=1;i<=col_num;i++)
	{
		if(!in[i])
		{
			q.push(i);
			dis[i]=size[i];
			ca[i]=1;
			if(dis[ans]<dis[i]) ans=i;
		}
	}
	while(!q.empty())
	{
		int u=q.front(); q.pop();
		for(int i=head[u];i;i=e[i].nxt)
		{
			int to=e[i].to;
			--in[to];
			if(dis[to]<dis[u]+size[to])
			{
				ca[to]=0;
				dis[to]=dis[u]+size[to];
				if(dis[ans]<dis[to]) ans=to;
			}
			if(dis[to]==dis[u]+size[to])
			{
				ca[to]=(ca[to]+ca[u])%x;
			}
			if(!in[to]) q.push(to);
		}
	}
}
int main() 
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d%d%d",&n,&m,&x);
	for(int i=1;i<=m;i++)
	{
		scanf("%d%d",&f[i],&t[i]);
		add(f[i],t[i]);
	}
	for(int i=1;i<=n;i++)
		if(!dfn[i])
			tarjan(i);
	addedge();
	topo();
	printf("%d\n",dis[ans]);
	int anss=0;
	for(int i=1;i<=col_num;i++)
		if(dis[ans]==dis[i])
			anss=(anss+ca[i])%x;
	printf("%d",anss);	
	return 0;
}