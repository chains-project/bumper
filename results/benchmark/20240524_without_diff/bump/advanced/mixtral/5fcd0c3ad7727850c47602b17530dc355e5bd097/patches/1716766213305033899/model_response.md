Here is a possible patch for the failing client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

This patch uses the `getClassInfoFor` method instead of `getClassInfo`, which was added in a later version of the `CoverageDatabase` class. This method takes a single `ClassName` argument instead of a `Set<ClassName>`, which matches the argument type of the original `getClassInfo` call.