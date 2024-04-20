Here's the suggested patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    byte[] classfile = coverage.getClassfile(className);
    long timestamp = coverage.getTimestamp(className);
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, classfile, timestamp);
}
```

This patch introduces a new helper method `getClassInfoFromCoverage` that utilizes the new `getClassInfo` method added in the updated library version. It takes the `CoverageDatabase` and `ClassName` as input and returns the `ClassInfo`. The `createSummaryData` method is updated to use the new helper method.