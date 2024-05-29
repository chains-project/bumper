Here is a possible patch for the code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

This patch uses the new method `getClassInfoFor` that was added in the `CoverageDatabase` class to replace the deprecated method `getClassInfo`. This method takes a single `ClassName` argument instead of a `Set<ClassName>`, which is more appropriate for the use case here.