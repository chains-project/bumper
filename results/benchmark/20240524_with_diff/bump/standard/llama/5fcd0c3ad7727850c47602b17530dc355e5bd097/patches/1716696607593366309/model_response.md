Here is the proposed patch:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassName className = data.getMutatedClass();
    byte[] classBytes = coverage.getClassBytes(className);
    long classModifiers = coverage.getClassModifiers(className);
    org.pitest.classinfo.ClassInfo classInfo = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(className, classBytes, classModifiers);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```