Here's the proposed patch:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverage(), coverage.getTimeStamp());
}
```

The `getClassInfo` method was removed from `CoverageDatabase`, so I created a new helper method `getClassInfoFromCoverage` to obtain the `ClassInfo` using the new method `getClassInfo` from `ClassInfoVisitor`.