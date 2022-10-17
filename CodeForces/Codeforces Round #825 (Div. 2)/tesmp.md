This is the hard version of this problem. In this version, we have queries. Note that we do not have multiple test cases in this version. You can make hacks only if both versions of the problem are solved.

An array $$$b$$$ of length $$$m$$$ is good if for all $$$i$$$ the $$$i$$$-th element is greater than or equal to $$$i$$$. In other words, $$$b$$$ is good if and only if $$$b_i \geq i$$$ for all $$$i$$$ ($$$1 \leq i \leq m$$$).

You are given an array $$$a$$$ consisting of $$$n$$$ positive integers, and you are asked $$$q$$$ queries.

In each query, you are given two integers $$$p$$$ and $$$x$$$ ($$$1 \leq p,x \leq n$$$). You have to do $$$a_p := x$$$ (assign $$$x$$$ to $$$a_p$$$). In the updated array, find the number of pairs of indices $$$(l, r)$$$, where $$$1 \le l \le r \le n$$$, such that the array $$$[a_l, a_{l+1}, \ldots, a_r]$$$ is good.

Note that all queries are independent, which means after each query, the initial array $$$a$$$ is restored.