private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    final var className = data.getMutatedClass().getClassName();
    final var classInfo = coverage.accept(new org.pitest.classinfo.ClassInfoVisitor(), className, new byte[0], 0);
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}