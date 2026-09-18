import {api} from './client'
import type {UseCaseRecord} from './models'

export const getUseCase=(applicationId:string)=>api<UseCaseRecord>(`/api/use-cases/${encodeURIComponent(applicationId)}`)
export const getUseCases=()=>api<UseCaseRecord[]>('/api/use-cases')