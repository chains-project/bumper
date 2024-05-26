Here is a possible patch for the failing client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

In this patch, I replaced the method `getClassInfo` with `getClassInfoFor`, which is a new method added in the `CoverageDatabase` interface. This method takes a single `ClassName` argument instead of a `Set<ClassName>`. This should fix the "cannot find symbol" error.