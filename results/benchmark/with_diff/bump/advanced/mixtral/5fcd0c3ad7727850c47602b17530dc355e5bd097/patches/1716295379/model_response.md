Here is a possible patch for the failing client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfo(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfo(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverageData(className), coverage.getTimeOfLastCoverage());
}
```

This patch introduces a new helper method `getClassInfo` that uses the new `getClassInfo` method added to `ClassInfoVisitor` to build a `ClassInfo` object from the `CoverageDatabase` and the mutated class name. This method is then used in the `createSummaryData` method to build the `MutationTestSummaryData` object.