Here is a patch that you can apply to the code to fix the error:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoFor(data.getMutatedClass()));
}
```

This patch fixes the error by using the `getClassInfoFor` method instead of `getClassInfo`, which was deprecated in a recent version of the `org.pitest.coverage` library. The `getClassInfoFor` method takes a single `org.pitest.classinfo.ClassName` parameter, which is equivalent to the `Set` of class names that was passed to the deprecated `getClassInfo` method.