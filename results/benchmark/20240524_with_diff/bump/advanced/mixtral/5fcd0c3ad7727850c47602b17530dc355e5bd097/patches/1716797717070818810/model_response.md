Here's the proposed patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfosFromCoverage(coverage, data.getMutatedClass()));
}

private java.util.List<org.pitest.classinfo.ClassInfo> getClassInfosFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfo.from(className, coverage.getRawCoverage(className).toByteArray(), coverage.getTimestamp(className));
}
```

This patch introduces a new helper method `getClassInfosFromCoverage` to replace the removed `getClassInfo` method from `CoverageDatabase`. The new method uses the added `ClassInfo.from` static method to build the required `ClassInfo` instances.