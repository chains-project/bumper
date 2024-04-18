Here's the proposed patch to fix the error:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverageData(className), coverage.getTimestamp());
}
```

This patch introduces a new helper method `getClassInfoFromCoverage` that uses the new `getClassInfo` method from `ClassInfoVisitor` to obtain the required `ClassInfo` object using the raw coverage data and timestamp from the `CoverageDatabase`. This method replaces the direct usage of the removed `getClassInfo` method from `CoverageDatabase`.