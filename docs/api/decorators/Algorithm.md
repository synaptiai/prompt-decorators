# Algorithm Decorator

Implements specific algorithms with the desired complexity characteristics.

**Category**: Code Generation

## Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|--------|
| `type` | enum | Algorithm category | context-dependent |
| `complexity` | enum | Desired time complexity | best-available |
| `approach` | enum | Algorithm design approach | most-appropriate |

## Type Options

- `sorting`: Use a sorting algorithm such as merge sort, quick sort, or bubble sort.
- `search`: Implement a search algorithm such as binary search, linear search, or depth-first search.
- `graph`: Use a graph algorithm such as Dijkstra's, BFS, DFS, or minimum spanning tree.
- `string`: Implement a string processing algorithm such as KMP, Rabin-Karp, or regex matching.
- `numeric`: Use a numeric algorithm such as GCD, prime factorization, or numerical integration.
- `ml`: Implement a machine learning algorithm such as linear regression, k-means, or neural networks.
- `crypto`: Use a cryptographic algorithm such as RSA, AES, or hashing functions.

## Complexity Options

- `constant`: The algorithm should have O(1) time complexity.
- `logarithmic`: The algorithm should have O(log n) time complexity.
- `linear`: The algorithm should have O(n) time complexity.
- `linearithmic`: The algorithm should have O(n log n) time complexity.
- `quadratic`: The algorithm should have O(n²) time complexity.
- `polynomial`: The algorithm should have polynomial time complexity.
- `exponential`: The algorithm may have exponential time complexity if necessary.

## Approach Options

- `recursive`: Implement the algorithm using a recursive approach.
- `iterative`: Implement the algorithm using an iterative approach.
- `divide-conquer`: Use a divide and conquer strategy for the implementation.
- `dynamic`: Implement the algorithm using dynamic programming techniques.
- `greedy`: Use a greedy algorithm approach for the implementation.

## Examples

### Implementing a graph algorithm with linear complexity using an iterative approach

```
+++Algorithm(type=graph, complexity=linear, approach=iterative)
Implement an algorithm to find the shortest path between two nodes in an unweighted graph.
```

The model will implement a breadth-first search algorithm for finding the shortest path in an unweighted graph, using an iterative approach with O(n) time complexity.

### Implementing a sorting algorithm with optimal complexity

```
+++Algorithm(type=sorting, complexity=linearithmic)
Implement a stable sorting algorithm for an array of integers.
```

The model will implement a merge sort algorithm, which is stable and has O(n log n) time complexity.

## Model-Specific Implementations

### gpt-3.5-turbo

**Instruction:** Write code for an algorithm with these specifications:

**Notes:** This model may need more explicit instructions about algorithm implementation details.

### gpt-4

**Instruction:** Implement an algorithm with the following characteristics:

**Notes:** This model can handle more abstract algorithm descriptions and infer appropriate implementations.


## Compatibility

- **Requires**: None
- **Conflicts**: None
- **Compatible Models**: gpt-3.5-turbo, gpt-4, claude-2, llama-2
- **Standard Version**: 1.0.0 - 2.0.0

## Related Decorators

- **CodeStyle**: Enhances Algorithm CodeStyle can be used to specify the coding style for the algorithm implementation.
- **Language**: Enhances Algorithm Language can be used to specify the programming language for the algorithm implementation.
