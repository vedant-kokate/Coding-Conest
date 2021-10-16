#include <bits/stdc++.h>
#include <bits/extc++.h>

using namespace std;
using namespace __gnu_pbds;

#define all(x) (x).begin(), (x).end()
#define fro(i, a, n, s) for (int i = (a); i < (n); i += (s))
#define fr(i, a, n) for (int i = (a); i < (n); i += (1))
#define frbo(i, a, n, s) for (int i = (a); i >= (n); i -= (s))
#define frb(i, a, n) for (int i = (a); i >= (n); i -= (1))
#define sz(x) (int)(x).size()
#define trav(a, x) for (auto &a : x)
#define csbits(x) __builtin_popcountll(x)
#define mk(arr, n, type) type *arr = new type[n]

#define str string
#define li long int
#define uli unsigned long int
#define ll long long
#define ull unsigned long long
#define ld long double
#define pll pair<ll, ll>
#define vl vector<ll>
#define v vector
#define vpl vector<pll>
#define msll multiset<ll>
#define mpll map<ll, ll>
#define umap unordered_map
#define pqll priority_queue<ll>

#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define ppb pop_back
#define pf push_front
#define ppf pop_front
#define eb emplace_back
#define lb lower_bound

#define ed '\n'
#define sp " \n"[i == n - 1]
#define null NULL
#define nulp nullptr

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
typedef tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update> pbds;

template <typename T>
ostream &operator<<(ostream &os, const vector<T> &v)
{
    os << "[";
    trav(x, v)
    {
        os << x << " ";
    }
    os << "]\n";
    return os;
}

template <typename T, typename S>
ostream &operator<<(ostream &os, const map<T, S> &v)
{
    os << "{";
    trav(x, v)
    {
        os << x.ff << ":" << x.ss << ", ";
    }
    os << "}\n";
    return os;
}

template <typename T, typename S>
ostream &operator<<(ostream &os, const pair<T, S> &x)
{
    os << "(" << x.ff << "," << x.ss << ")\n";
    return os;
}

template <typename T>
T const pi = std::acos(-T(1));
#define MAX 100005
#define MOD 1000000007 // 998244353
#define INF 1e18 + 1
ll d8[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
ll d4[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

//#define ONLINE_JUDGE 1
/*
    g++ c1.cpp -o c1.exe
    g++ -o c1 c1.cpp&c1.exe
*/

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin.exceptions(cin.failbit);

    // clock_t start, end;
    // start = clock();

    ll __;
    cout << "ooo1";
    cin >> __;
    fr(_, 0, __)
    {
        cout << "ooo";
        ll n, m, c, ans = 0;
        cin >> n >> m;
        // vl s(m + 1, 0);
        v<vl> p(n + 1, vl(m + 1, 0));
        cout << p;
        fr(i, 0, m)
        {
            cin >> c;
            p[0][c]++;
        }
        fr(i, 1, n + 1)
        {
            fr(j, 0, m)
            {
                cin >> c;
                p[i][c]++;
            }
        }
        fr(i, 1, n)
        {
            fr(j, 0, m)
            {
                if (p[i][j] == 0)
                    continue;
                if (p[i - 1][j] < p[i][j])
                    ans += p[i][j] - p[i - 1][j];
            }
        }
        fr(j, 0, m)
        {
            if (p[n][j] == 0)
                continue;
            if (p[n - 1][j] < p[n][j])
                ans -= p[n - 1][j];
        }

        cout << "Case #" << _ + 1 << ": " << ans << ed;
    }

    // end = clock();
    // cout << "Time taken: " << fixed << double(end - start) / double(CLOCKS_PER_SEC) << setprecision(5) << " sec";

    return 0;
}