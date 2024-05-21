Here's a possible patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

The patch replaces the `getClassInfo` method with the new method `getClassInfoFor`, which was added in the `CoverageDatabase` class. The `getClassInfoFor` method takes a single `ClassName` argument instead of a `Set<ClassName>`. This change should fix the "cannot find symbol" error.