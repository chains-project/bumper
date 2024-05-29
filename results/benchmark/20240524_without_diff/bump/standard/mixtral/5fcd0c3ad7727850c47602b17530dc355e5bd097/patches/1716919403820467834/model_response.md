Here's the proposed patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

The patch modifies the code to use the `getClassInfoFor` method instead of `getClassInfo`, as the latter is no longer available in the updated dependency. This should resolve the "cannot find symbol" error.