Here is the proposed patch:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverageDatabase(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverageDatabase(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    byte[] classfile = coverage.getClassFile(className);
    long timestamp = coverage.getTimestamp(className);
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, classfile, timestamp);
}
```

This patch introduces a new helper method `getClassInfoFromCoverageDatabase` that retrieves the `ClassInfo` from the `CoverageDatabase` using the new `getClassInfo` method added in the new library version. The `createSummaryData` method is updated to use this helper method instead of calling `getClassInfo` directly on the `CoverageDatabase`.