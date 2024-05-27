Here's a fixed version of the method using an added library method `getAllClassInfo()` to get all class information from the `CoverageDatabase` object:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getAllClassInfo().get(data.getMutatedClass()));
}
```

This should resolve the "cannot find symbol" error caused by the missing `getClassInfo()` method.