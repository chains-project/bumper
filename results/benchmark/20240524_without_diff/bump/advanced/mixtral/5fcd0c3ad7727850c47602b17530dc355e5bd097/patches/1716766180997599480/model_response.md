Here's a possible patch for the given client code:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```
The patch replaces the `getClassInfo` method with `getClassInfoFor`, which is the new method added in the external dependency. The `getClassInfoFor` method takes a single `ClassName` argument instead of a `Set<ClassName>` argument.