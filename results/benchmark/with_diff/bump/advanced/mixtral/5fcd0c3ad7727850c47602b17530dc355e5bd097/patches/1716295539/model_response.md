Here's the updated `createSummaryData` method that should fix the error:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverageData(className), coverage.getTimestamp());
}
```

The `getClassInfo` method from `CoverageDatabase` has been removed, so I created a helper method `getClassInfoFromCoverage` that uses the new `getClassInfo` method from `ClassInfoVisitor`. This method takes the `ClassName` and raw coverage data, which can be obtained from `CoverageDatabase`.