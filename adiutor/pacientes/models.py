from django.db import models

class terapeutas(models.Model):
    Nome = models.CharField(max_length=20)
    # CRP 12/ _ _ _ _ _
    Crp = models.CharField(max_length=5)
    Senha = models.CharField(max_length=10)

    def __str__(self):
        return self.Nome

    class Meta:
        verbose_name = "Terapeutas"
        verbose_name_plural = "Terapeutas"

class pacientes(models.Model):
    Id = models.IntegerField(primary_key=True)
    Nome = models.CharField(max_length=200)
    Responsavel = models.CharField(max_length=255, blank=True, null=True)
    Parentesco = models.CharField(max_length=200, blank=True, null=True)
    Nascimento = models.DateField()
    SEX = (
        ('MASCULINO', 'Masculino'),
        ('FEMININO', 'Feminino'),
    )
    Sexo = models.CharField(max_length=20, choices=SEX)
    Cadastro = models.DateField()
    Terapeuta = models.ForeignKey(terapeutas, on_delete=models.CASCADE)
    Inicio = models.DateField()
    Termino = models.DateField(blank=True, null=True)
    STATUS = (
        ('ANAMNESE', 'Deve ser feita anamnese'),
        ('ATENDIMENTO', 'Está sendo atendido'),
        ('LICENCA', 'Em licença'),
        ('ENCERRADO', 'Encerrado'),
    )
    Status = models.CharField(max_length=15, choices=STATUS, default='ANAMNESE')
    Agendamento = models.IntegerField()
    CONVENIOS = (
        ('UNIMED', 'UNIMED'),
        ('AGEMED', 'AGEMED'),
        ('ABEPOM', 'ABEPOM'),
        ('PARTICULAR', 'Particular'),
        ('LOCUS', 'LOCUS'),
        ('ELASE', 'ELASE'),
        ('CORTESIA', 'Cortesia'),
    )
    Convenio = models.CharField(max_length=20, choices=CONVENIOS)
    MOD = (
        ('INDIVIDUAL', 'Individual'),
        ('CASAL', 'Casal'),
        ('FAMILIA', 'Familia'),
        ('GRUPO', 'Grupo'),
        ('AVALIACAO', 'Avaliação'),
    )
    Modalidade = models.CharField(max_length=20, choices=MOD)
    Celular = models.IntegerField(blank=True, null=True)
    Whats = models.IntegerField( blank=True, null=True)
    Fixo = models.IntegerField(blank=True, null=True)
    Email = models.EmailField(max_length=40)
    CIVIL = (
        ('SOLTEIRO', 'Solteiro'),
        ('CASADO', 'Casado'),
        ('DIVORCIADO', 'Divorciado'),
        ('VIUVO', 'Viúvo'),
        ('UNIAO-ESTAVEL', 'União Estável'),
    )
    EstadoCivil = models.CharField(max_length=20, choices=CIVIL)
    Profissao = models.CharField(max_length=100)
    Rua = models.CharField(max_length=255)
    Numero = models.CharField(max_length=255)
    Complemento = models.CharField(max_length=255)
    Bairro = models.CharField(max_length=255)
    Cidade = models.CharField(max_length=255)
    Estado = models.CharField(max_length=2)
    Observacao = models.TextField()

    def __str__(self):
        return self.Nome

    class Meta:
        verbose_name = "Pacientes"
        verbose_name_plural = "Pacientes"
