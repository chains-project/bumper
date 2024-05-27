Here's the proposed patch:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

Explanation:

The error message indicates that the method `getClassInfo` with a `Set<ClassName>` parameter is not found in the `CoverageDatabase` class.

Instead, we can use the method `getClassInfoFor` with a `ClassName` parameter, which is available in the same class.

By changing the method call from `getClassInfo` to `getClassInfoFor`, we can fix the error and make the code compile.