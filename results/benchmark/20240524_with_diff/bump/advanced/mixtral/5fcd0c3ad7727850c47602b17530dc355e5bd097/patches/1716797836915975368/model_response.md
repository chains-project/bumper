Here is a potential patch for the code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawCoverage(className), coverage.getTimestamp());
}
```

This patch introduces a new helper method `getClassInfoFromCoverage` that uses the new `getClassInfo` method added to `ClassInfoVisitor` to get the `ClassInfo` for the given class name. This method takes the raw coverage data and timestamp from the `CoverageDatabase` as input. The `createSummaryData` method is then updated to use this helper method to get the `ClassInfo` for the mutated class.

Note that this patch assumes that the `CoverageDatabase` implementation used in the code has a `getRawCoverage` method that returns a byte array representing the raw coverage data for the given class name. If this method is not available, a different approach may be necessary.