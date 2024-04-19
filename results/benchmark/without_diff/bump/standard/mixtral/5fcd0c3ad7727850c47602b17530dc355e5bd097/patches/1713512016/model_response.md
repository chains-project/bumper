Here's a proposed patch for the client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

This patch uses the `getClassInfoFor` method instead of `getClassInfo`, which was added in a later version of the library. The `getClassInfoFor` method takes a single `ClassName` argument instead of a `Set<ClassName>`, so we can pass `data.getMutatedClass()` directly.