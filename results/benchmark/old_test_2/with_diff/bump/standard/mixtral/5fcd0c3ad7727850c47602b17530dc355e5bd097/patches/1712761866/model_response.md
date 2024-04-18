Here's a proposed patch for the client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverage(className), coverage.getTimestamp());
}
```

This patch introduces a new helper method `getClassInfoFromCoverage` that uses the new `getClassInfo` method in `ClassInfoVisitor` to obtain the `ClassInfo` object. This method takes a `CoverageDatabase` and a `ClassName` as input and returns the corresponding `ClassInfo`. The `createSummaryData` method is updated to use this helper method instead of the removed `getClassInfo` method in `CoverageDatabase`.