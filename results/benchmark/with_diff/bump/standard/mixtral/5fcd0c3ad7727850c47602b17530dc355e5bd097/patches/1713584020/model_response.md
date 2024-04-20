Here's the proposed patch for the client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, coverage.getRawData(className), coverage.getTimestamp(className));
}
```

The patch introduces a new helper method `getClassInfoFromCoverage` that uses the `getClassInfo` static method from `ClassInfoVisitor` to get the `ClassInfo` for the given class name. The `getClassInfo` method in `CoverageDatabase` has been removed, so we need to use the new method to get the `ClassInfo`.