Here is a potential patch for the code you provided:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

This patch uses the `getClassInfoFor` method, which was added in a later version of the library and should be available in the version you are using. The `getClassInfo` method, which was used in the original code, has been removed and is no longer available.