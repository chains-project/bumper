```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final org.pitest.classinfo.ClassName className = org.pitest.classinfo.ClassName.fromString(data.getMutatedClass());
    final byte[] bytecode = coverage.getBytecodeForClass(className).orElse(new byte[0]);
    final org.pitest.classinfo.ClassInfo classInfo = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, bytecode, data.getTimestamp());

    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), java.util.Collections.singletonList(classInfo));
}
```