Here is a possible patch for the code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

The change I made is to replace the method `getClassInfo` with `getClassInfoFor`, which is an added method in the `CoverageDatabase` interface. This method takes a single `ClassName` argument, which is what `data.getMutatedClass()` returns.