Here's a possible patch for the client code to fix the error:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverageData(className), coverage.getTimestamp());
}
```

The patch creates a new helper method `getClassInfoFromCoverage` that uses the new `getClassInfo` method from `ClassInfoVisitor` to get the `ClassInfo` for the given class name and coverage data. The original `createSummaryData` method is then updated to use the new helper method instead of calling `getClassInfo` directly on the `CoverageDatabase`.