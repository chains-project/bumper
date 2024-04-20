Here's the proposed patch for the given client code:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverage(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverage(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    byte[] classfileBytes = coverage.getClassfileBytes(className);
    long timestamp = coverage.getTimestamp(className);
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, classfileBytes, timestamp);
}
```

The patch modifies the original `createSummaryData` method by introducing a new helper method `getClassInfoFromCoverage`. This new method retrieves the classfile bytes and timestamp from the `coverage` object and then calls the new `getClassInfo` method from `ClassInfoVisitor` to build the `ClassInfo` object. The `createSummaryData` method now uses the new helper method to get the `ClassInfo`.