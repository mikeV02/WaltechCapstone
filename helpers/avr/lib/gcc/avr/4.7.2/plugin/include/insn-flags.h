/* Generated automatically by the program `genflags'
   from the machine description file `md'.  */

#ifndef GCC_INSN_FLAGS_H
#define GCC_INSN_FLAGS_H

#define HAVE_pushqi1 1
#define HAVE_load_qi_libgcc 1
#define HAVE_load_hi_libgcc 1
#define HAVE_load_si_libgcc 1
#define HAVE_load_sf_libgcc 1
#define HAVE_load_psi_libgcc 1
#define HAVE_load_qi ((CONST_INT_P (operands[1]) && AVR_HAVE_LPMX) \
   || (REG_P (operands[1]) && AVR_HAVE_ELPMX))
#define HAVE_load_hi ((CONST_INT_P (operands[1]) && AVR_HAVE_LPMX) \
   || (REG_P (operands[1]) && AVR_HAVE_ELPMX))
#define HAVE_load_si ((CONST_INT_P (operands[1]) && AVR_HAVE_LPMX) \
   || (REG_P (operands[1]) && AVR_HAVE_ELPMX))
#define HAVE_load_sf ((CONST_INT_P (operands[1]) && AVR_HAVE_LPMX) \
   || (REG_P (operands[1]) && AVR_HAVE_ELPMX))
#define HAVE_load_psi ((CONST_INT_P (operands[1]) && AVR_HAVE_LPMX) \
   || (REG_P (operands[1]) && AVR_HAVE_ELPMX))
#define HAVE_load_qi_clobber (!((CONST_INT_P (operands[1]) && AVR_HAVE_LPMX) \
     || (REG_P (operands[1]) && AVR_HAVE_ELPMX)))
#define HAVE_load_hi_clobber (!((CONST_INT_P (operands[1]) && AVR_HAVE_LPMX) \
     || (REG_P (operands[1]) && AVR_HAVE_ELPMX)))
#define HAVE_load_si_clobber (!((CONST_INT_P (operands[1]) && AVR_HAVE_LPMX) \
     || (REG_P (operands[1]) && AVR_HAVE_ELPMX)))
#define HAVE_load_sf_clobber (!((CONST_INT_P (operands[1]) && AVR_HAVE_LPMX) \
     || (REG_P (operands[1]) && AVR_HAVE_ELPMX)))
#define HAVE_load_psi_clobber (!((CONST_INT_P (operands[1]) && AVR_HAVE_LPMX) \
     || (REG_P (operands[1]) && AVR_HAVE_ELPMX)))
#define HAVE_xload8_A (can_create_pseudo_p() \
   && !avr_xload_libgcc_p (QImode) \
   && avr_mem_memx_p (operands[1]) \
   && REG_P (XEXP (operands[1], 0)))
#define HAVE_xloadqi_A (can_create_pseudo_p() \
   && avr_mem_memx_p (operands[1]) \
   && REG_P (XEXP (operands[1], 0)))
#define HAVE_xloadhi_A (can_create_pseudo_p() \
   && avr_mem_memx_p (operands[1]) \
   && REG_P (XEXP (operands[1], 0)))
#define HAVE_xloadsi_A (can_create_pseudo_p() \
   && avr_mem_memx_p (operands[1]) \
   && REG_P (XEXP (operands[1], 0)))
#define HAVE_xloadsf_A (can_create_pseudo_p() \
   && avr_mem_memx_p (operands[1]) \
   && REG_P (XEXP (operands[1], 0)))
#define HAVE_xloadpsi_A (can_create_pseudo_p() \
   && avr_mem_memx_p (operands[1]) \
   && REG_P (XEXP (operands[1], 0)))
#define HAVE_xload_8 (!avr_xload_libgcc_p (QImode))
#define HAVE_xload_qi_libgcc (avr_xload_libgcc_p (QImode))
#define HAVE_xload_hi_libgcc (avr_xload_libgcc_p (HImode))
#define HAVE_xload_si_libgcc (avr_xload_libgcc_p (SImode))
#define HAVE_xload_sf_libgcc (avr_xload_libgcc_p (SFmode))
#define HAVE_xload_psi_libgcc (avr_xload_libgcc_p (PSImode))
#define HAVE_movqi_insn (register_operand (operands[0], QImode) \
   || register_operand (operands[1], QImode) \
   || const0_rtx == operands[1])
#define HAVE_movhi_sp_r 1
#define HAVE_movmem_qi 1
#define HAVE_movmem_hi 1
#define HAVE_movmemx_qi 1
#define HAVE_movmemx_hi 1
#define HAVE_addqi3 1
#define HAVE_addhi3_clobber 1
#define HAVE_addsi3 1
#define HAVE_addpsi3 1
#define HAVE_subpsi3 1
#define HAVE_subqi3 1
#define HAVE_subhi3 1
#define HAVE_subsi3 1
#define HAVE_smulqi3_highpart (AVR_HAVE_MUL)
#define HAVE_umulqi3_highpart (AVR_HAVE_MUL)
#define HAVE_mulqihi3 (AVR_HAVE_MUL)
#define HAVE_umulqihi3 (AVR_HAVE_MUL)
#define HAVE_usmulqihi3 (AVR_HAVE_MUL)
#define HAVE_mulsqihi3 (AVR_HAVE_MUL)
#define HAVE_muluqihi3 (AVR_HAVE_MUL)
#define HAVE_muloqihi3 (AVR_HAVE_MUL)
#define HAVE_muluqisi3 (AVR_HAVE_MUL && !reload_completed)
#define HAVE_muluhisi3 (AVR_HAVE_MUL && !reload_completed)
#define HAVE_mulsqisi3 (AVR_HAVE_MUL && !reload_completed)
#define HAVE_mulshisi3 (AVR_HAVE_MUL && !reload_completed)
#define HAVE_mulohisi3 (AVR_HAVE_MUL && !reload_completed)
#define HAVE_divmodqi4 1
#define HAVE_udivmodqi4 1
#define HAVE_divmodhi4 1
#define HAVE_udivmodhi4 1
#define HAVE_mulsqipsi3 (AVR_HAVE_MUL && !reload_completed)
#define HAVE_divmodpsi4 1
#define HAVE_udivmodpsi4 1
#define HAVE_divmodsi4 1
#define HAVE_udivmodsi4 1
#define HAVE_andqi3 1
#define HAVE_andhi3 1
#define HAVE_andpsi3 1
#define HAVE_andsi3 1
#define HAVE_iorqi3 1
#define HAVE_iorhi3 1
#define HAVE_iorpsi3 1
#define HAVE_iorsi3 1
#define HAVE_xorqi3 1
#define HAVE_xorhi3 1
#define HAVE_xorpsi3 1
#define HAVE_xorsi3 1
#define HAVE_ashlhi3 1
#define HAVE_ashlsi3 1
#define HAVE_ashrqi3 1
#define HAVE_ashrhi3 1
#define HAVE_ashrpsi3 1
#define HAVE_ashrsi3 1
#define HAVE_lshrhi3 1
#define HAVE_lshrpsi3 1
#define HAVE_lshrsi3 1
#define HAVE_absqi2 1
#define HAVE_abssf2 1
#define HAVE_negqi2 1
#define HAVE_neghi2 1
#define HAVE_negpsi2 1
#define HAVE_negsi2 1
#define HAVE_negsf2 1
#define HAVE_one_cmplqi2 1
#define HAVE_one_cmplhi2 1
#define HAVE_one_cmplpsi2 1
#define HAVE_one_cmplsi2 1
#define HAVE_extendqihi2 1
#define HAVE_extendqipsi2 1
#define HAVE_extendqisi2 1
#define HAVE_extendhipsi2 1
#define HAVE_extendhisi2 1
#define HAVE_extendpsisi2 1
#define HAVE_zero_extendqihi2 1
#define HAVE_zero_extendqipsi2 1
#define HAVE_zero_extendqisi2 1
#define HAVE_zero_extendhipsi2 1
#define HAVE_n_extendhipsi2 1
#define HAVE_zero_extendhisi2 1
#define HAVE_zero_extendpsisi2 1
#define HAVE_zero_extendqidi2 1
#define HAVE_zero_extendhidi2 1
#define HAVE_zero_extendsidi2 1
#define HAVE_branch 1
#define HAVE_branch_unspec 1
#define HAVE_difficult_branch 1
#define HAVE_rvbranch 1
#define HAVE_difficult_rvbranch 1
#define HAVE_jump 1
#define HAVE_call_insn 1
#define HAVE_call_value_insn 1
#define HAVE_nop 1
#define HAVE_sez 1
#define HAVE_popqi 1
#define HAVE_cli_sei 1
#define HAVE_call_prologue_saves 1
#define HAVE_epilogue_restores 1
#define HAVE_return (reload_completed && avr_simple_epilogue ())
#define HAVE_return_from_epilogue ((reload_completed  \
    && cfun->machine  \
    && !(cfun->machine->is_interrupt || cfun->machine->is_signal) \
    && !cfun->machine->is_naked))
#define HAVE_return_from_interrupt_epilogue ((reload_completed  \
    && cfun->machine  \
    && (cfun->machine->is_interrupt || cfun->machine->is_signal) \
    && !cfun->machine->is_naked))
#define HAVE_return_from_naked_epilogue ((reload_completed  \
    && cfun->machine  \
    && cfun->machine->is_naked))
#define HAVE_delay_cycles_1 1
#define HAVE_delay_cycles_2 1
#define HAVE_delay_cycles_3 1
#define HAVE_delay_cycles_4 1
#define HAVE_insert_bits 1
#define HAVE_copysignsf3 1
#define HAVE_fmul_insn (AVR_HAVE_MUL)
#define HAVE_fmuls_insn (AVR_HAVE_MUL)
#define HAVE_fmulsu_insn (AVR_HAVE_MUL)
#define HAVE_adddi3_insn (avr_have_dimode)
#define HAVE_adddi3_const8_insn (avr_have_dimode)
#define HAVE_adddi3_const_insn (avr_have_dimode \
   && !s8_operand (operands[0], VOIDmode))
#define HAVE_subdi3_insn (avr_have_dimode)
#define HAVE_negdi2_insn (avr_have_dimode)
#define HAVE_compare_di2 (avr_have_dimode)
#define HAVE_compare_const8_di2 (avr_have_dimode)
#define HAVE_compare_const_di2 (avr_have_dimode \
   && !s8_operand (operands[0], VOIDmode))
#define HAVE_ashldi3_insn (avr_have_dimode)
#define HAVE_ashrdi3_insn (avr_have_dimode)
#define HAVE_lshrdi3_insn (avr_have_dimode)
#define HAVE_rotldi3_insn (avr_have_dimode)
#define HAVE_nonlocal_goto_receiver 1
#define HAVE_nonlocal_goto 1
#define HAVE_pushcqi1 1
#define HAVE_pushhi1 1
#define HAVE_pushchi1 1
#define HAVE_pushpsi1 1
#define HAVE_pushsi1 1
#define HAVE_pushcsi1 1
#define HAVE_pushdi1 1
#define HAVE_pushcdi1 1
#define HAVE_pushsf1 1
#define HAVE_pushsc1 1
#define HAVE_movqi 1
#define HAVE_movhi 1
#define HAVE_movsi 1
#define HAVE_movsf 1
#define HAVE_movpsi 1
#define HAVE_movmemhi 1
#define HAVE_setmemhi 1
#define HAVE_strlenhi 1
#define HAVE_addhi3 1
#define HAVE_mulqi3 1
#define HAVE_mulqi3_call 1
#define HAVE_mulhi3 1
#define HAVE_mulhi3_call 1
#define HAVE_mulsi3 (AVR_HAVE_MUL)
#define HAVE_mulhisi3 (AVR_HAVE_MUL)
#define HAVE_umulhisi3 (AVR_HAVE_MUL)
#define HAVE_usmulhisi3 (AVR_HAVE_MUL)
#define HAVE_smulhi3_highpart (AVR_HAVE_MUL)
#define HAVE_umulhi3_highpart (AVR_HAVE_MUL)
#define HAVE_mulpsi3 (AVR_HAVE_MUL)
#define HAVE_rotlqi3 1
#define HAVE_rotlqi3_4 1
#define HAVE_rotlhi3 1
#define HAVE_rotlpsi3 1
#define HAVE_rotlsi3 1
#define HAVE_ashlqi3 1
#define HAVE_ashlpsi3 1
#define HAVE_lshrqi3 1
#define HAVE_cbranchsi4 1
#define HAVE_cbranchpsi4 1
#define HAVE_cbranchhi4 1
#define HAVE_cbranchqi4 1
#define HAVE_call 1
#define HAVE_sibcall 1
#define HAVE_call_value 1
#define HAVE_sibcall_value 1
#define HAVE_indirect_jump 1
#define HAVE_casesi 1
#define HAVE_enable_interrupt 1
#define HAVE_disable_interrupt 1
#define HAVE_prologue 1
#define HAVE_epilogue 1
#define HAVE_sibcall_epilogue 1
#define HAVE_flash_segment1 1
#define HAVE_flash_segment 1
#define HAVE_parityhi2 1
#define HAVE_paritysi2 1
#define HAVE_popcounthi2 1
#define HAVE_popcountsi2 1
#define HAVE_clzhi2 1
#define HAVE_clzsi2 1
#define HAVE_ctzhi2 1
#define HAVE_ctzsi2 1
#define HAVE_ffshi2 1
#define HAVE_ffssi2 1
#define HAVE_bswapsi2 1
#define HAVE_nopv 1
#define HAVE_sleep 1
#define HAVE_wdr 1
#define HAVE_fmul 1
#define HAVE_fmuls 1
#define HAVE_fmulsu 1
#define HAVE_insv (optimize)
#define HAVE_extzv 1
#define HAVE_adddi3 (avr_have_dimode)
#define HAVE_subdi3 (avr_have_dimode)
#define HAVE_negdi2 (avr_have_dimode)
#define HAVE_conditional_jump (avr_have_dimode)
#define HAVE_cbranchdi4 (avr_have_dimode)
#define HAVE_ashldi3 (avr_have_dimode)
#define HAVE_ashrdi3 (avr_have_dimode)
#define HAVE_lshrdi3 (avr_have_dimode)
#define HAVE_rotldi3 (avr_have_dimode)
extern rtx        gen_pushqi1                        (rtx);
extern rtx        gen_load_qi_libgcc                 (void);
extern rtx        gen_load_hi_libgcc                 (void);
extern rtx        gen_load_si_libgcc                 (void);
extern rtx        gen_load_sf_libgcc                 (void);
extern rtx        gen_load_psi_libgcc                (void);
extern rtx        gen_load_qi                        (rtx, rtx);
extern rtx        gen_load_hi                        (rtx, rtx);
extern rtx        gen_load_si                        (rtx, rtx);
extern rtx        gen_load_sf                        (rtx, rtx);
extern rtx        gen_load_psi                       (rtx, rtx);
extern rtx        gen_load_qi_clobber                (rtx, rtx);
extern rtx        gen_load_hi_clobber                (rtx, rtx);
extern rtx        gen_load_si_clobber                (rtx, rtx);
extern rtx        gen_load_sf_clobber                (rtx, rtx);
extern rtx        gen_load_psi_clobber               (rtx, rtx);
extern rtx        gen_xload8_A                       (rtx, rtx);
extern rtx        gen_xloadqi_A                      (rtx, rtx);
extern rtx        gen_xloadhi_A                      (rtx, rtx);
extern rtx        gen_xloadsi_A                      (rtx, rtx);
extern rtx        gen_xloadsf_A                      (rtx, rtx);
extern rtx        gen_xloadpsi_A                     (rtx, rtx);
extern rtx        gen_xload_8                        (rtx, rtx);
extern rtx        gen_xload_qi_libgcc                (void);
extern rtx        gen_xload_hi_libgcc                (void);
extern rtx        gen_xload_si_libgcc                (void);
extern rtx        gen_xload_sf_libgcc                (void);
extern rtx        gen_xload_psi_libgcc               (void);
extern rtx        gen_movqi_insn                     (rtx, rtx);
extern rtx        gen_movhi_sp_r                     (rtx, rtx, rtx);
extern rtx        gen_movmem_qi                      (rtx, rtx, rtx);
extern rtx        gen_movmem_hi                      (rtx, rtx, rtx);
extern rtx        gen_movmemx_qi                     (rtx, rtx);
extern rtx        gen_movmemx_hi                     (rtx, rtx);
extern rtx        gen_addqi3                         (rtx, rtx, rtx);
extern rtx        gen_addhi3_clobber                 (rtx, rtx, rtx);
extern rtx        gen_addsi3                         (rtx, rtx, rtx);
extern rtx        gen_addpsi3                        (rtx, rtx, rtx);
extern rtx        gen_subpsi3                        (rtx, rtx, rtx);
extern rtx        gen_subqi3                         (rtx, rtx, rtx);
extern rtx        gen_subhi3                         (rtx, rtx, rtx);
extern rtx        gen_subsi3                         (rtx, rtx, rtx);
extern rtx        gen_smulqi3_highpart               (rtx, rtx, rtx);
extern rtx        gen_umulqi3_highpart               (rtx, rtx, rtx);
extern rtx        gen_mulqihi3                       (rtx, rtx, rtx);
extern rtx        gen_umulqihi3                      (rtx, rtx, rtx);
extern rtx        gen_usmulqihi3                     (rtx, rtx, rtx);
extern rtx        gen_mulsqihi3                      (rtx, rtx, rtx);
extern rtx        gen_muluqihi3                      (rtx, rtx, rtx);
extern rtx        gen_muloqihi3                      (rtx, rtx, rtx);
extern rtx        gen_muluqisi3                      (rtx, rtx, rtx);
extern rtx        gen_muluhisi3                      (rtx, rtx, rtx);
extern rtx        gen_mulsqisi3                      (rtx, rtx, rtx);
extern rtx        gen_mulshisi3                      (rtx, rtx, rtx);
extern rtx        gen_mulohisi3                      (rtx, rtx, rtx);
extern rtx        gen_divmodqi4                      (rtx, rtx, rtx, rtx);
extern rtx        gen_udivmodqi4                     (rtx, rtx, rtx, rtx);
extern rtx        gen_divmodhi4                      (rtx, rtx, rtx, rtx);
extern rtx        gen_udivmodhi4                     (rtx, rtx, rtx, rtx);
extern rtx        gen_mulsqipsi3                     (rtx, rtx, rtx);
extern rtx        gen_divmodpsi4                     (rtx, rtx, rtx, rtx);
extern rtx        gen_udivmodpsi4                    (rtx, rtx, rtx, rtx);
extern rtx        gen_divmodsi4                      (rtx, rtx, rtx, rtx);
extern rtx        gen_udivmodsi4                     (rtx, rtx, rtx, rtx);
extern rtx        gen_andqi3                         (rtx, rtx, rtx);
extern rtx        gen_andhi3                         (rtx, rtx, rtx);
extern rtx        gen_andpsi3                        (rtx, rtx, rtx);
extern rtx        gen_andsi3                         (rtx, rtx, rtx);
extern rtx        gen_iorqi3                         (rtx, rtx, rtx);
extern rtx        gen_iorhi3                         (rtx, rtx, rtx);
extern rtx        gen_iorpsi3                        (rtx, rtx, rtx);
extern rtx        gen_iorsi3                         (rtx, rtx, rtx);
extern rtx        gen_xorqi3                         (rtx, rtx, rtx);
extern rtx        gen_xorhi3                         (rtx, rtx, rtx);
extern rtx        gen_xorpsi3                        (rtx, rtx, rtx);
extern rtx        gen_xorsi3                         (rtx, rtx, rtx);
extern rtx        gen_ashlhi3                        (rtx, rtx, rtx);
extern rtx        gen_ashlsi3                        (rtx, rtx, rtx);
extern rtx        gen_ashrqi3                        (rtx, rtx, rtx);
extern rtx        gen_ashrhi3                        (rtx, rtx, rtx);
extern rtx        gen_ashrpsi3                       (rtx, rtx, rtx);
extern rtx        gen_ashrsi3                        (rtx, rtx, rtx);
extern rtx        gen_lshrhi3                        (rtx, rtx, rtx);
extern rtx        gen_lshrpsi3                       (rtx, rtx, rtx);
extern rtx        gen_lshrsi3                        (rtx, rtx, rtx);
extern rtx        gen_absqi2                         (rtx, rtx);
extern rtx        gen_abssf2                         (rtx, rtx);
extern rtx        gen_negqi2                         (rtx, rtx);
extern rtx        gen_neghi2                         (rtx, rtx);
extern rtx        gen_negpsi2                        (rtx, rtx);
extern rtx        gen_negsi2                         (rtx, rtx);
extern rtx        gen_negsf2                         (rtx, rtx);
extern rtx        gen_one_cmplqi2                    (rtx, rtx);
extern rtx        gen_one_cmplhi2                    (rtx, rtx);
extern rtx        gen_one_cmplpsi2                   (rtx, rtx);
extern rtx        gen_one_cmplsi2                    (rtx, rtx);
extern rtx        gen_extendqihi2                    (rtx, rtx);
extern rtx        gen_extendqipsi2                   (rtx, rtx);
extern rtx        gen_extendqisi2                    (rtx, rtx);
extern rtx        gen_extendhipsi2                   (rtx, rtx);
extern rtx        gen_extendhisi2                    (rtx, rtx);
extern rtx        gen_extendpsisi2                   (rtx, rtx);
extern rtx        gen_zero_extendqihi2               (rtx, rtx);
extern rtx        gen_zero_extendqipsi2              (rtx, rtx);
extern rtx        gen_zero_extendqisi2               (rtx, rtx);
extern rtx        gen_zero_extendhipsi2              (rtx, rtx);
extern rtx        gen_n_extendhipsi2                 (rtx, rtx, rtx);
extern rtx        gen_zero_extendhisi2               (rtx, rtx);
extern rtx        gen_zero_extendpsisi2              (rtx, rtx);
extern rtx        gen_zero_extendqidi2               (rtx, rtx);
extern rtx        gen_zero_extendhidi2               (rtx, rtx);
extern rtx        gen_zero_extendsidi2               (rtx, rtx);
extern rtx        gen_branch                         (rtx, rtx);
extern rtx        gen_branch_unspec                  (rtx, rtx);
extern rtx        gen_difficult_branch               (rtx, rtx);
extern rtx        gen_rvbranch                       (rtx, rtx);
extern rtx        gen_difficult_rvbranch             (rtx, rtx);
extern rtx        gen_jump                           (rtx);
extern rtx        gen_call_insn                      (rtx, rtx, rtx);
extern rtx        gen_call_value_insn                (rtx, rtx, rtx, rtx);
extern rtx        gen_nop                            (void);
extern rtx        gen_sez                            (void);
extern rtx        gen_popqi                          (rtx);
extern rtx        gen_cli_sei                        (rtx, rtx);
extern rtx        gen_call_prologue_saves            (rtx, rtx);
extern rtx        gen_epilogue_restores              (rtx);
extern rtx        gen_return                         (void);
extern rtx        gen_return_from_epilogue           (void);
extern rtx        gen_return_from_interrupt_epilogue (void);
extern rtx        gen_return_from_naked_epilogue     (void);
extern rtx        gen_delay_cycles_1                 (rtx, rtx);
extern rtx        gen_delay_cycles_2                 (rtx, rtx);
extern rtx        gen_delay_cycles_3                 (rtx, rtx);
extern rtx        gen_delay_cycles_4                 (rtx, rtx);
extern rtx        gen_insert_bits                    (rtx, rtx, rtx, rtx);
extern rtx        gen_copysignsf3                    (rtx, rtx, rtx);
extern rtx        gen_fmul_insn                      (rtx, rtx, rtx);
extern rtx        gen_fmuls_insn                     (rtx, rtx, rtx);
extern rtx        gen_fmulsu_insn                    (rtx, rtx, rtx);
extern rtx        gen_adddi3_insn                    (void);
extern rtx        gen_adddi3_const8_insn             (void);
extern rtx        gen_adddi3_const_insn              (rtx);
extern rtx        gen_subdi3_insn                    (void);
extern rtx        gen_negdi2_insn                    (void);
extern rtx        gen_compare_di2                    (void);
extern rtx        gen_compare_const8_di2             (void);
extern rtx        gen_compare_const_di2              (rtx);
extern rtx        gen_ashldi3_insn                   (void);
extern rtx        gen_ashrdi3_insn                   (void);
extern rtx        gen_lshrdi3_insn                   (void);
extern rtx        gen_rotldi3_insn                   (void);
extern rtx        gen_nonlocal_goto_receiver         (void);
extern rtx        gen_nonlocal_goto                  (rtx, rtx, rtx, rtx);
extern rtx        gen_pushcqi1                       (rtx);
extern rtx        gen_pushhi1                        (rtx);
extern rtx        gen_pushchi1                       (rtx);
extern rtx        gen_pushpsi1                       (rtx);
extern rtx        gen_pushsi1                        (rtx);
extern rtx        gen_pushcsi1                       (rtx);
extern rtx        gen_pushdi1                        (rtx);
extern rtx        gen_pushcdi1                       (rtx);
extern rtx        gen_pushsf1                        (rtx);
extern rtx        gen_pushsc1                        (rtx);
extern rtx        gen_movqi                          (rtx, rtx);
extern rtx        gen_movhi                          (rtx, rtx);
extern rtx        gen_movsi                          (rtx, rtx);
extern rtx        gen_movsf                          (rtx, rtx);
extern rtx        gen_movpsi                         (rtx, rtx);
extern rtx        gen_movmemhi                       (rtx, rtx, rtx, rtx);
extern rtx        gen_setmemhi                       (rtx, rtx, rtx, rtx);
extern rtx        gen_strlenhi                       (rtx, rtx, rtx, rtx);
extern rtx        gen_addhi3                         (rtx, rtx, rtx);
extern rtx        gen_mulqi3                         (rtx, rtx, rtx);
extern rtx        gen_mulqi3_call                    (rtx, rtx, rtx);
extern rtx        gen_mulhi3                         (rtx, rtx, rtx);
extern rtx        gen_mulhi3_call                    (rtx, rtx, rtx);
extern rtx        gen_mulsi3                         (rtx, rtx, rtx);
extern rtx        gen_mulhisi3                       (rtx, rtx, rtx);
extern rtx        gen_umulhisi3                      (rtx, rtx, rtx);
extern rtx        gen_usmulhisi3                     (rtx, rtx, rtx);
extern rtx        gen_smulhi3_highpart               (rtx, rtx, rtx);
extern rtx        gen_umulhi3_highpart               (rtx, rtx, rtx);
extern rtx        gen_mulpsi3                        (rtx, rtx, rtx);
extern rtx        gen_rotlqi3                        (rtx, rtx, rtx);
extern rtx        gen_rotlqi3_4                      (rtx, rtx);
extern rtx        gen_rotlhi3                        (rtx, rtx, rtx);
extern rtx        gen_rotlpsi3                       (rtx, rtx, rtx);
extern rtx        gen_rotlsi3                        (rtx, rtx, rtx);
extern rtx        gen_ashlqi3                        (rtx, rtx, rtx);
extern rtx        gen_ashlpsi3                       (rtx, rtx, rtx);
extern rtx        gen_lshrqi3                        (rtx, rtx, rtx);
extern rtx        gen_cbranchsi4                     (rtx, rtx, rtx, rtx);
extern rtx        gen_cbranchpsi4                    (rtx, rtx, rtx, rtx);
extern rtx        gen_cbranchhi4                     (rtx, rtx, rtx, rtx);
extern rtx        gen_cbranchqi4                     (rtx, rtx, rtx, rtx);
#define GEN_CALL(A, B, C, D) gen_call ((A), (B))
extern rtx        gen_call                           (rtx, rtx);
#define GEN_SIBCALL(A, B, C, D) gen_sibcall ((A), (B))
extern rtx        gen_sibcall                        (rtx, rtx);
#define GEN_CALL_VALUE(A, B, C, D, E) gen_call_value ((A), (B), (C))
extern rtx        gen_call_value                     (rtx, rtx, rtx);
#define GEN_SIBCALL_VALUE(A, B, C, D, E) gen_sibcall_value ((A), (B), (C))
extern rtx        gen_sibcall_value                  (rtx, rtx, rtx);
extern rtx        gen_indirect_jump                  (rtx);
extern rtx        gen_casesi                         (rtx, rtx, rtx, rtx, rtx);
extern rtx        gen_enable_interrupt               (void);
extern rtx        gen_disable_interrupt              (void);
extern rtx        gen_prologue                       (void);
extern rtx        gen_epilogue                       (void);
extern rtx        gen_sibcall_epilogue               (void);
extern rtx        gen_flash_segment1                 (rtx, rtx, rtx);
extern rtx        gen_flash_segment                  (rtx, rtx);
extern rtx        gen_parityhi2                      (rtx, rtx);
extern rtx        gen_paritysi2                      (rtx, rtx);
extern rtx        gen_popcounthi2                    (rtx, rtx);
extern rtx        gen_popcountsi2                    (rtx, rtx);
extern rtx        gen_clzhi2                         (rtx, rtx);
extern rtx        gen_clzsi2                         (rtx, rtx);
extern rtx        gen_ctzhi2                         (rtx, rtx);
extern rtx        gen_ctzsi2                         (rtx, rtx);
extern rtx        gen_ffshi2                         (rtx, rtx);
extern rtx        gen_ffssi2                         (rtx, rtx);
extern rtx        gen_bswapsi2                       (rtx, rtx);
extern rtx        gen_nopv                           (rtx);
extern rtx        gen_sleep                          (void);
extern rtx        gen_wdr                            (void);
extern rtx        gen_fmul                           (rtx, rtx, rtx);
extern rtx        gen_fmuls                          (rtx, rtx, rtx);
extern rtx        gen_fmulsu                         (rtx, rtx, rtx);
extern rtx        gen_insv                           (rtx, rtx, rtx, rtx);
extern rtx        gen_extzv                          (rtx, rtx, rtx, rtx);
extern rtx        gen_adddi3                         (rtx, rtx, rtx);
extern rtx        gen_subdi3                         (rtx, rtx, rtx);
extern rtx        gen_negdi2                         (rtx, rtx);
extern rtx        gen_conditional_jump               (rtx, rtx);
extern rtx        gen_cbranchdi4                     (rtx, rtx, rtx, rtx);
extern rtx        gen_ashldi3                        (rtx, rtx, rtx);
extern rtx        gen_ashrdi3                        (rtx, rtx, rtx);
extern rtx        gen_lshrdi3                        (rtx, rtx, rtx);
extern rtx        gen_rotldi3                        (rtx, rtx, rtx);

#endif /* GCC_INSN_FLAGS_H */
