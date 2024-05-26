Here's the proposed patch to fix the error:

```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), getClassInfoFromCoverageDatabase(coverage, data.getMutatedClass()));
}

private org.pitest.classinfo.ClassInfo getClassInfoFromCoverageDatabase(org.pitest.coverage.CoverageDatabase coverage, org.pitest.classinfo.ClassName className) {
    byte[] classfileBytes = coverage.getRawClassFile(className);
    return org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, classfileBytes, coverage.getTimestamp(className));
}
```

The `getClassInfo` method of `CoverageDatabase` has been removed, so we need to manually extract the classfile bytes and timestamp from `CoverageDatabase` and use the new `getClassInfo` static method of `ClassInfoVisitor` to get the `ClassInfo` object.