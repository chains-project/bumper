Here's a potential patch for the issue. It seems that the method `getClassInfo` is not available for the `coverage` object of type `CoverageDatabase`. Instead, we can use the method `getClassCoverage` and then extract the required class information from the `ClassCoverage` object:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.coverage.ClassCoverage classCoverage = coverage.getClassCoverage(data.getMutatedClass());
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classCoverage.getClassInfo());
}
```

This code uses the `getClassCoverage` method to get the `ClassCoverage` object, which has the `getClassInfo` method. This should resolve the symbol not found error.