Here is a possible patch for the code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

This patch uses the method `getClassInfoFor` instead of `getClassInfo`, as the latter seems to be deprecated or not present in the version of the library you are using. The `getClassInfoFor` method takes a single `ClassName` argument, which is what `data.getMutatedClass()` returns, so this should be a drop-in replacement for the original code.