Here is a potential patch for the failing client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

The `getClassInfo` method has been replaced with `getClassInfoFor` in the `coverage` object, which is a new method added in the external dependency. This should fix the error and allow the code to compile.