Here is a possible patch for the failing client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

This patch uses the new method `getClassInfoFor` that was added in `CoverageDatabase` to replace the deprecated `getClassInfo` method. The `getClassInfoFor` method takes a single `ClassName` argument rather than a `Set<ClassName>`.