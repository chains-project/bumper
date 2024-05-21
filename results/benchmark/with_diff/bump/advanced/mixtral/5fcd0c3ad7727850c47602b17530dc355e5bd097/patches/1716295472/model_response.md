Here's a possible patch for the failing client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverage(className), coverage.getTimestamp());
}
```

In this patch, we create a new helper method `getClassInfoFromCoverage` that uses the new `getClassInfo` method added in the library. We pass the `CoverageDatabase`'s raw coverage data and timestamp to this method to get the corresponding `ClassInfo`. We then use this `ClassInfo` to create the `MutationTestSummaryData` object.