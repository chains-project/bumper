Here's the proposed patch for the failing client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverageData(className), coverage.getTimestamp());
}
```

The changes include:

1. Creating a new helper method `getClassInfoFromCoverage` that accepts `CoverageDatabase` and `ClassName` and returns `ClassInfo`.
2. Using the new method `getClassInfo` from `ClassInfoVisitor` to get the `ClassInfo` using the raw coverage data and timestamp.