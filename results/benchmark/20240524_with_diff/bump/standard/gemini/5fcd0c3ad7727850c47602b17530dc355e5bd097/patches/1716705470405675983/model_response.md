```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder classInfo = null;
    for (org.pitest.classinfo.ClassName name : java.util.Collections.singleton(data.getMutatedClass())) {
        classInfo = coverage.getClassInfo(name);
        if (classInfo != null) {
            break;
        }
    }
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```